let React = require('react');
let FlipCard = require('react-flipcard');
var Card = React.createClass({
  render: function(){
    return(
        <FlipCard>
          {/* The first child is used as the front of the card */}
          <div>
            <h4 className="about-h4"><strong>{this.props.heading}</strong></h4>
            <div className="section-icon"><this.props.icon /></div>
          </div>
          {/* The second child is used as the back of the card */}
          <div>
            <p>{this.props.content}</p>
          </div>
        </FlipCard>
    );
  }
});
module.exports = Card;