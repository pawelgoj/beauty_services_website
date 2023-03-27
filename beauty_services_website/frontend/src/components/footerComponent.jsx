import React, { Component } from 'react';

// Names of components must be written using capital letter.
function FooterComponent({ status, body }) {
    console.log('status: ', status);
    console.log('body: ', body);
    return (
        <footer>
            {(status === 200) ?
                <>
                    <div className="container-fluid bg-secondary">
                        {body.map((item) => (
                            <div>
                                <a style={{ color: 'black', }} href={item.link}>{item.name}</a>
                            </div>
                        ))}
                        <div><span>tel. xxxxxxxxxxx</span></div>
                        <div><span>email: xxxx@xxxx.com</span></div>
                    </div> </> : <div></div>}
        </footer>
    );
}

export default FooterComponent;
