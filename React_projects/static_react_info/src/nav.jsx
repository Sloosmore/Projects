import reactlogo from "./assets/react.svg";
import "./nav.css";

function Nav() {
  return (
    <nav className="nav">
      <div className="logo">
        <img src={reactlogo} alt="react_logo med-font" className="pic" />
        <h3 className="company-name">ReactFacts</h3>
      </div>
      <h4 className="test">Loosmore 1 - React page</h4>
    </nav>
  );
}

export default Nav;
