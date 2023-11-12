import "./content.css";
import People_Grid from "./assets/people_grid.png";

function Content() {
  return (
    <>
      <div className="reduce">
        <div className="img_grid">
          <img src={People_Grid} alt="" />
        </div>
      </div>
      <div className="pad_text">
        <h1>Online Expirences</h1>
        <p>
          Join a unique interactive activities led by one of a kind hosts-all
          without leaving home
        </p>
      </div>
    </>
  );
}

export default Content;
