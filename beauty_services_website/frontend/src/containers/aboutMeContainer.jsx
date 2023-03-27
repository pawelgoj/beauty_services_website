import React, { Component, useState, useEffect } from 'react';
import AboutMeComponent from '../components/aboutMeComponent';

// Names of components must be written using capital letter.
const ABOUT_ME_URL = "/business/omnie"



const AboutMeContainer = () => {
    const [aboutMe, setState] = useState({ status: "", body: "" });
    const fetchData = () => {
        fetch(ABOUT_ME_URL, { method: "GET" })
            .then(res => {
                res.json().then(data => {
                    setState({ status: res.status, body: data.results });
                })
            })
            .catch(err => { setState(err) });
    }
    useEffect(fetchData, []);

    return (
        <AboutMeComponent status={aboutMe.status} body={aboutMe.body} />
    );
};


export default AboutMeContainer;