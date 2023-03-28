import React, { Component, useState, useEffect } from 'react';
import FooterComponent from '../components/footerComponent';

// Names of components must be written using capital letter.
const SOCIAL_MEDIA_URL = "/business/social_data"


const FooterContainer = () => {
    const [socialMedia, setState] = useState({ status: "", socialMedia: "", myContact: ""});
    const fetchData = () => {
        fetch(SOCIAL_MEDIA_URL, { method: "GET" })
            .then(res => {
                res.json().then(data => {
                    setState({ status: res.status, 
                               socialMedia: data.results.social_media,
                               myContact: data.results.my_contact});
                })
            }).catch(err => { setState(err) });
    }
    useEffect(fetchData, []);

    return (
        <FooterComponent status={socialMedia.status} socialMedia={socialMedia.socialMedia}
        myContact={socialMedia.myContact} />
    );
};


export default FooterContainer;