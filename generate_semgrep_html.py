import json
import os
from datetime import datetime

# HTML template with embedded CSS
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Semgrep Scan Report - {directory}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f9;
        }}
        h1 {{
            color: #333;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background-color: #fff;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border: 1px solid #ddd;
        }}
        th {{
            background-color: #4CAF50;
            color: white;
        }}
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        .severity-error {{ background-color: #f8d7da; }}
        .severity-warning {{ background-color: #fff3cd; }}
        .severity-info {{ background-color: #d1ecf1; }}
        .summary {{
            margin-bottom: 20px;
            font-size: 1.1em;
        }}
        a {{
            color: #0066cc;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <h1>Semgrep Scan Report - {directory}</h1>
    <div class="summary">
        <p><strong>Scan Date:</strong> {scan_date}</p>
        <p><strong>Total Findings:</strong> {total_findings}</p>
        <p><strong>Severity Breakdown:</strong> Errors: {errors}, Warnings: {warnings}, Info: {info}</p>
    </div>
    <table>
        <tr>
            <th>Rule ID</th>
            <th>Severity</th>
            <th>Message</th>
            <th>File</th>
            <th>Line</th>
            <th>Details</th>
        </tr>
        {table_rows}
    </table>
</body>
</html>
"""

def generate_semgrep_html(json_file, output_html, directory):
    # Read Semgrep JSON output
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Extract findings
    findings = data.get('results', [])
    
    # Calculate summary
    total_findings = len(findings)
    errors = sum(1 for f in findings if f.get('severity') == 'ERROR')
    warnings = sum(1 for f in findings if f.get('severity') == 'WARNING')
    info = sum(1 for f in findings if f.get('severity') == 'INFO')
    
    # Generate table rows
    table_rows = ''
    for finding in findings:
        rule_id = finding.get('check_id', 'N/A')
        severity = finding.get('severity', 'N/A')
        message = finding.get('message', 'No message')
        file_path = finding.get('path', 'N/A')
        line = finding.get('start', {}).get('line', 'N/A')
        details_url = finding.get('extra', {}).get('metadata', {}).get('source', 'N/A')
        
        # Assign severity class for styling
        severity_class = {
            'ERROR': 'severity-error',
            'WARNING': 'severity-warning',
            'INFO': 'severity-info'
        }.get(severity, '')
        
        table_rows += f"""
        <tr class="{severity_class}">
            <td>{rule_id}</td>
            <td>{severity}</td>
            <td>{message}</td>
            <td>{file_path}</td>
            <td>{line}</td>
            <td><a href="{details_url}" target="_blank">View Details</a></td>
        </tr>
        """

    # Populate HTML template
    html_content = HTML_TEMPLATE.format(
        directory=directory,
        scan_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        total_findings=total_findings,
        errors=errors,
        warnings=warnings,
        info=info,
        table_rows=table_rows
    )

    # Write to output HTML file
    with open(output_html, 'w') as f:
        f.write(html_content)

# Example usage for one directory
if __name__ == "__main__":
    import sys
    json_file = sys.argv[1]
    output_html = sys.argv[2]
    directory = sys.argv[3]
    generate_semgrep_html(json_file, output_html, directory)
