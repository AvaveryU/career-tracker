import { Offline, Online } from 'react-detect-offline';

import {
  Route,
  createBrowserRouter,
  createRoutesFromElements,
} from 'react-router-dom';
import Root from './root';
import ErrorBoundary from './ErrorBoundary';

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route
      path="/"
      element={
        <>
          <Online>
            <Root />
          </Online>
          <Offline>
            <ErrorBoundary />
          </Offline>
        </>
      }
      errorElement={<ErrorBoundary />}
    >
      {/* Main Page */}
      <Route index element={<p>Здесь мейн пейдж</p>} />

      {/*  Роут для проверки своих компонентов в адресной строке ввест /test */}
      <Route path="test" element={<p>Сюда вставлять тестовый компонент</p>} />
    </Route>,
  ),
);
export default router;
