import React, { Component } from 'react';
import { Grid, Row, Tabs, Tab } from 'react-bootstrap';
import TeamMember from './team-member.jsx';
import { teamMembers,  hallOfFame } from './team-directory.jsx';
import { settings } from './react-slick-settings.jsx';
const Slider = require('react-slick');

class Team extends Component {

  render() {
    return (
      <Grid id="team">
        <Row className="show-grid">
          <Tabs defaultActiveKey={1} id="team-tab">
            <Tab eventKey={1} title="Team Members">
              <Slider {...settings}>
                {teamMembers.map((member, i) => {
                  return (
                    <div key={i}><TeamMember {...member}/></div>
                  )
                })}
              </Slider>
            </Tab>
            <Tab eventKey={2} title="Hall Of Fame">
              <Slider {...settings}>
                {hallOfFame.map((member, i) => {
                  return (
                    <div key={i}><TeamMember {...member}/></div>
                  )
                })}
              </Slider>
            </Tab>
          </Tabs>
        </Row>
      </Grid>
    )
  }
}

export default Team;
