import React, { Component } from 'react';
import { Grid, Row, Tabs, Tab } from 'react-bootstrap';
import TeamMember from './team-member.jsx';
var Slider = require('react-slick');


class Team extends Component {

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
                  twitter: 'https://twitter.com/',
                  github: 'https://github.com/andela-mochieng',
                  linkedin: '#',

              },
              {
                  name: 'Abdulwahab Abdulmalik',
                  position: 'Developer',
                  imgSrc: 'https://avatars3.githubusercontent.com/u/17270426?v=3&s=245',
                  twitter: 'https://twitter.com/',
                  github: 'https://github.com/andela-aabdulwahab',
                  linkedin: '#',

              },
              {
                  name: 'Hassan Oyeboade',
                  position: 'Developer',
                  imgSrc: 'https://avatars1.githubusercontent.com/u/18309948?v=3&s=245',
                  twitter: 'https://twitter.com/',
                  github: 'https://github.com/andela-hoyeboade',
                  linkedin: '#',

              },
              {
                  name: 'Chukwuerika Dike',
                  position: 'Developer',
                  imgSrc: 'https://avatars2.githubusercontent.com/u/7263503?v=3&s=245',
                  twitter: 'https://twitter.com/@rikkydyke',
                  github: 'https://github.com/andela-cdike',
                  linkedin: '#',

              },
              {
                  name: 'Jimmy Kamau',
                  position: 'Developer',
                  imgSrc: 'https://avatars2.githubusercontent.com/u/20517534?v=3&s=245',
                  twitter: 'https://twitter.com/@kamau_jimmy',
                  github: 'https://github.com/andela-jkamau',
                  linkedin: '#',

              },
              {
                  name: 'Loice Andia Kivisi',
                  position: 'Developer',
                  imgSrc: 'https://avatars1.githubusercontent.com/u/20776933?v=3&s=245',
                  twitter: 'https://twitter.com/@AndiaLoice',
                  github: 'https://github.com/andela-lolo',
                  linkedin: '#',

              },
              {
                  name: 'Chibuzor Obiora',
                  position: 'Team Lead',
                  imgSrc: 'https://avatars3.githubusercontent.com/u/8373338?v=3&s=245',
                  twitter: 'https://twitter.com/',
                  github: 'https://github.com/andela-cobiora',
                  linkedin: '#',

              },
              {
                  name: 'Njira Perci',
                  position: 'Project Manager',
                  imgSrc: 'https://avatars2.githubusercontent.com/u/2056512?v=3&s=245',
                  twitter: 'https://twitter.com/',
                  github: 'https://github.com/njirap',
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

            }
        ];
    return(
    <Grid id="team">
      <Row className="show-grid">
        <Tabs defaultActiveKey={1} id="team-tab">
          <Tab eventKey={1} title="Team Members">
            <Slider {...settings}>
              {teams.map((member, i) => {
                return(<div><TeamMember {...member} /></div>)
              })}
            </Slider>
          </Tab>
          <Tab eventKey={2} title="Hall Of Fame">
            <Slider {...settings}>
              {hallOfFame.map((member, i) => {
                return(<div><TeamMember {...member} /></div>)
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
