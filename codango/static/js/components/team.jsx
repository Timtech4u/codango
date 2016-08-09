import React, {Component} from 'react';
import { Grid, Row, Tabs, Tab } from 'react-bootstrap';
var Slider = require('react-slick');


class TeamMember extends Component {
  render() {
    return (
      <div>
        <div className="team-img-container" >
          <img src={this.props.imgSrc} />
          <div className="team-social-container" >
            <div className="team-social-wrapper" >
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


export default class Team extends Component {

  render(){
      var settings = {
          dots: false,
          infinite: true,
          speed: 500,
          slidesToShow: 4,
          slidesToScroll: 1,
          autoplay: false,
          responsive: [{
              breakpoint: 1024,
              settings: {
                  slidesToShow: 3,
                  slidesToScroll: 3,
                  infinite: true,
              }
          }, {
              breakpoint: 700,
              settings: {
                  slidesToShow: 2,
                  slidesToScroll: 2
              }
          }, {
              breakpoint: 480,
              settings: {
                  slidesToShow: 1,
                  slidesToScroll: 1
              }
          }]
      };
      var teams = [
              {
                  name: 'Margaret Ochieng',
                  position: 'Developer',
                  imgSrc: 'https://avatars2.githubusercontent.com/u/12407721?v=3&s=245',
                  twitter: '#',
                  github: 'https://github.com/andela-mochieng',
                  linkedin: '#',

              },
              {
                  name: 'Abdulwahab Abdulmalik',
                  position: 'Developer',
                  imgSrc: 'https://avatars3.githubusercontent.com/u/17270426?v=3&s=245',
                  twitter: '#',
                  github: 'https://github.com/andela-aabdulwahab',
                  linkedin: '#',

              },
              {
                  name: 'Alex Kiura',
                  position: 'Developer',
                  imgSrc: 'https://avatars2.githubusercontent.com/u/17288133?v=3&s=245',
                  twitter: '#',
                  github: 'https://github.com/andela-akiura',
                  linkedin: '#',

              },
              {
                  name: 'Nwuguru Sunday',
                  position: 'Developer',
                  imgSrc: 'https://avatars0.githubusercontent.com/u/18328313?v=3&s=245',
                  twitter: '#',
                  github: 'https://github.com/andela-snwuguru',
                  linkedin: '#',

              },
              {
                  name: 'Hassan Oyeboade',
                  position: 'Developer',
                  imgSrc: 'https://avatars1.githubusercontent.com/u/18309948?v=3&s=245',
                  twitter: '#',
                  github: 'https://github.com/andela-hoyeboade',
                  linkedin: '#',

              }
          ];
        var hallOfFame = [
            {
                name: 'Chidiebere Nnadi',
                position: 'Developer',
                imgSrc: 'https://avatars1.githubusercontent.com/u/3100850?v=3&s=245',
                twitter: '#',
                github: 'https://github.com/andela-cnnadi',
                linkedin: '#',

            },
            {
                name: 'Stanley Ndagi',
                position: 'Developer',
                imgSrc: 'https://avatars2.githubusercontent.com/u/15629602?v=3&s=245',
                twitter: '#',
                github: 'https://github.com/NdagiStanley',
                linkedin: '#',

            },
            {
                name: 'Issa Jubril',
                position: 'Developer',
                imgSrc: 'https://avatars2.githubusercontent.com/u/13223950?v=3&s=245',
                twitter: '#',
                github: 'https://github.com/andela-ijubril',
                linkedin: '#',

            },
            {
                name: 'Olufunmilade Oshodi',
                position: 'Developer',
                imgSrc: 'https://avatars2.githubusercontent.com/u/13224175?v=3&s=245',
                twitter: '#',
                github: 'https://github.com/andela-ooshodi',
                linkedin: '#',

            },
            {
                name: 'Achile Egbunu',
                position: 'Developer',
                imgSrc: 'https://avatars1.githubusercontent.com/u/9017229?v=3&s=245',
                twitter: '#',
                github: 'https://github.com/Achile',
                linkedin: '#',

            },
            {
                name: 'Abiodun Shuaib',
                position: 'Developer',
                imgSrc: 'https://avatars2.githubusercontent.com/u/15088852?v=3&s=245',
                twitter: '#',
                github: 'https://github.com/andela-ashuaib',
                linkedin: '#',

            },
            {
                name: 'Joan Ngatia',
                position: 'Developer',
                imgSrc: 'https://avatars3.githubusercontent.com/u/13269579?v=3&s=245',
                twitter: '#',
                github: 'https://github.com/andela-jngatia',
                linkedin: '#',

            },
            {
                name: 'Ini-Oluwa C. Fageyinbo',
                position: 'Developer',
                imgSrc: 'https://avatars2.githubusercontent.com/u/13224913?v=3&s=245',
                twitter: '#',
                github: 'https://github.com/IniOluwa',
                linkedin: '#',

            },
        ];
    return(
    <Grid id="team">
      <Row className="show-grid">
        <Tabs defaultActiveKey={1} id="team-tab">
          <Tab eventKey={1} title="Team Members">
            <Slider {...settings}>
              {teams.map((member) => {
                return(<div><TeamMember {...member}/></div>)
              })}
            </Slider>
          </Tab>
          <Tab eventKey={2} title="Hall Of Fame">
            <Slider {...settings}>
              {hallOfFame.map((member) => {
                return(<div><TeamMember {...member}/></div>)
              })}
            </Slider>
          </Tab>
        </Tabs>
      </Row>
    </Grid>
    )
  }
}
