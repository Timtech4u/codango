import React, { Component } from 'react';

class TeamMember extends Component {
  render() {
    return (
      <div>
        <div className="team-img-container">
          <img src={this.props.imgSrc} />
          <div className="team-social-container">
            <div className="team-social-wrapper">
              <a href={this.props.twitter}><span className="mdi mdi-twitter"></span></a>
              <a href={this.props.github}><span className="mdi mdi-github-box"></span></a>
              <a href={this.props.linkedin}><span className="mdi mdi-linkedin"></span></a>
            </div>
          </div>
        </div>
        <a href={this.props.github}><h3>{this.props.name}</h3></a>
        <p>{this.props.position}</p>
      </div>
    )
  }
}

export default TeamMember;
