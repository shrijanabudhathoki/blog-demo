import cors from 'cors';
import dotenv from 'dotenv';
import express, { Application } from 'express';

import appRouter from './routes';
import { notFound } from './middlewares/notFound';
import { errorHandler } from './middlewares/errorHandler';
import {loggerMiddleware, errorLogger} from './middlewares/loggerMiddleware';
// Clerk imports
import { ClerkExpressWithAuth } from '@clerk/clerk-sdk-node';

dotenv.config();

const app: Application = express();

app.use(express.json());
app.use(cors());

app.use(loggerMiddleware);

// Clerk middleware: attaches req.auth to all requests
app.use(ClerkExpressWithAuth());

app.use(appRouter);

app.use(notFound);
app.use(errorLogger);
app.use(errorHandler);

const PORT = process.env.PORT || 5000;

app.listen(PORT, () =>
  console.log(`Server running in ${process.env.NODE_ENV} mode on port ${PORT}`)
);

// Changes test