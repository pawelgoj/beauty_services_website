import React, { Component, useState, useEffect }  from 'react';
import AboutMeComponent from '../components/aboutMeComponent';

// Names of components must be written using capital letter.
const ABOUT_ME_URL = "/business/omnie"



const AboutMeContainer = () => {
    const [aboutMe, setState] = useState("");
    const fetchData = () => { 
        fetch(ABOUT_ME_URL, {method: "GET"})
            .then(res=>{setState(res); console.log("data:", res);})
            .catch(err => {setState(err)});
    }
    useEffect(fetchData, []);

    return (
        <AboutMeComponent data={aboutMe} />
    );


};


export default AboutMeContainer;

// export default None;