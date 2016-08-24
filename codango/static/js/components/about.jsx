let React = require('react');
let FlipCard = require('react-flipcard');
let Card = require('../components/about-card.jsx');
let Share = require('react-material-icons/icons/social/share');
let Community = require('react-material-icons/icons/social/people');
let Pair = require('react-material-icons/icons/action/code');
import {Grid} from 'react-bootstrap';

let Shares = () => (<Share color='#f26500'/>);
let Communities = () => (<Community color='#f26500'/>);
let Pairs = () => (<Pair color='#f26500'/>);
module.exports = Shares;
let About = React.createClass({
  getInitialState() {
    return {
      isFlipped: false,
      aboutContent: [
        {
          heading: 'Community',
          content: 'Codango is an ever expanding community of vibrant developers from different stacks and levels, helping each other grow to be even stronger developers',
          icon: Communities
        }, {
          heading: 'Sharing Resources',
          content: 'Codango provides a platform for developers from various stacks to upload PDFs, DOCS, code snippets and knowledgable updates making them available for all to learn and use. With endless resources available from the whole world, learning has never been easier.',
          icon: Shares
        }, {
          heading: 'Pair Programming',
          content: 'Codango provides a platform where developers can act as mentors to other developers in real time and help grow a community of stronger developers.',
          icon: Pairs
        }
      ]
    };
  },
  showBack() {
    this.setState({isFlipped: true});
  },
  showFront() {
    this.setState({isFlipped: false});
  },
  handleOnFlip(flipped) {
    if (flipped) {
      this.refs.backButton.focus();
    }
  },
  handleKeyDown(e) {
    if (this.state.isFlipped && e.keyCode === 27) {
      this.showFront();
    }
  },
  render() {
    return (
      <Grid className="top-margin">
        <div className="row">
          <div className="col-sm-12 col-lg-12">
            <h1 className="page-title">About us</h1>
          </div>
        </div>
        <div className="row">
          <div className="col-sm-12 col-md-12">
            <h3 className="page-description">
              <em>Codango is a social networking site that connects all types of developers allowing for sharing resources, joining various communities and pair programming</em>
            </h3>
          </div>
        </div>
        <div id="cards" className="cards">
          {this.state.aboutContent.map((cardInfo) => {
            return (<Card heading={cardInfo.heading} content={cardInfo.content} key={this.state.aboutContent.indexOf(cardInfo)} icon={cardInfo.icon}/>)
          })}
        </div>
      </Grid>

    );
  }
});

module.exports = About;
