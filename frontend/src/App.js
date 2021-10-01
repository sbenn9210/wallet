import "./App.css";
import { Route, Switch } from "react-router-dom";

import Navigation from "./components/navigation";
import routes from "./components/shared/routes";
import PrivateRoute from "./components/shared/privateRoute";
import { withRouter } from "react-router-dom";

function App({ location }) {
  return (
    <div className="App">
      {location.pathname !== "/login" && location.pathname !== "/register" && (
        <Navigation />
      )}
      <Switch>
        {routes.map((route, index) => {
          return route.protected === false ? (
            <Route
              exact
              key={index}
              path={route.path}
              component={route.component}
            />
          ) : (
            <PrivateRoute
              exact
              key={index}
              path={route.path}
              component={route.component}
            />
          );
        })}
      </Switch>
    </div>
  );
}

export default withRouter(App);
