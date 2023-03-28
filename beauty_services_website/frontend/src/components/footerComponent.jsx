import React, { Component } from 'react';
import "bootstrap-icons/font/bootstrap-icons.css";

// Names of components must be written using capital letter.
function FooterComponent({ status, socialMedia, myContact }) {
    const iconsSocialMedia = {
        Instagram: "bi bi-instagram",
        Facebook: "bi bi-facebook",
        Tiktok: "bi bi-tiktok",
        Pinterest: "bi bi-pinterest"
    };
    console.log('status: ', status);
    return (
        <footer id="bootstrap-overrides-navbar" className="container-fluid gap-2 justify-content-center py-3 bg-secondary">
            {(status === 200) ?
                <>
                    <div className="flex-row justify-content-center">
                        <div className="d-flex justify-content-center">
                            {socialMedia.map((item) => (
                                <div className="">
                                    <a className="flex-fill h5 px-2" href={item.link}>
                                        <i className={iconsSocialMedia[item.logo]}></i> {item.name}</a>
                                </div>
                            ))}
                        </div>
                        {(myContact.phone != "") ?
                            <div className="flex-fill h5">tel. {myContact.phone}</div>
                            : <></>
                        }
                        <div className="d-flex justify-content-center h5"><p>email:&nbsp;</p><a href={"mailto:" + myContact.email}>{myContact.email}</a></div>
                        <div className="d-flex justify-content-center h6">Written by Paweł Goj</div>
                    </div>
                </> : <div></div>}
        </footer>
    );
}

export default FooterComponent;