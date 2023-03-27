import React, { Component, useState, useEffect } from 'react';
import FooterComponent from '../components/footerComponent';

// Names of components must be written using capital letter.
const SOCIAL_MEDIA_URL = "/business/social_data"


const FooterContainer = () => {
    const [socialMedia, setState] = useState({ status: "", body: "" });
    const fetchData = () => {
        fetch(SOCIAL_MEDIA_URL, { method: "GET" })
            .then(res => {
                res.json().then(data => {
                    setState({ status: res.status, body: data.results });
                })
            })
            .catch(err => { setState(err) });
    }
    useEffect(fetchData, []);

    return (
        <FooterComponent status={socialMedia.status} body={socialMedia.body} />
    );
};


export default FooterContainer;