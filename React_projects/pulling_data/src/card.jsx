import star from "./assets/Star.png";
import mountian_bike from "../public/mountain_bike.png";
import "./card.css";

function Card() {
  return (
    <div className="card">
      <div>
        <img src={mountian_bike} alt="" className="card_img" />
        <p className="tag">Sold out</p>
      </div>
      <div>
        <div className="rate">
          <img src={star} alt="" className="star" />
          <p className="rating">5.0 &#40;6&#41; USA</p>
        </div>
        <p>Group Mountain Biking</p>
        <p>
          <strong>From $50</strong> / person
        </p>
      </div>
    </div>
  );
}

export default Card;
