import React, { Component }  from 'react';

// Names of components must be written using capital letter.
function FooterComponent(prop) {
    return (
        <footer>
            <div className="container-fluid bg-secondary">
                <div><a style={{color: 'black', }} href="">Instagram</a></div>
                <div><span>tel. xxxxxxxxxxx</span></div>
                <div><span>email: xxxx@xxxx.com</span></div>
            </div>

        </footer>
    );
}

export default FooterComponent;
