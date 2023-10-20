import { Outlet, Link } from 'react-router-dom';
function Root() {
  return (
    <div>
      <h1>Шапка</h1>
      <main>
        <Outlet />
      </main>

      {location.pathname === '/' ? (
        <Link to="/test" style={{ margin: '50px', flex: '0 0 auto' }}>
          <button>Страница с тестовым компонентом</button>
        </Link>
      ) : null}

      <footer />
    </div>
  );
}

export default Root;
