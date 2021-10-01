import Login from "../../pages/login";
import Main from "../../pages/main";
import Register from "../../pages/register";

const routes = [
  {
    path: "/",
    component: Main,
    protected: true,
  },
  {
    path: "/login",
    component: Login,
    protected: false,
  },
  {
    path: "/register",
    component: Register,
    protected: false,
  },
];

export default routes;
