import React, { Component } from 'react';
import './aboutMe.css'

// Names of components must be written using capital letter.
function AboutMeComponent({ status, body }) {
    let image = "data:image/png;base64," + body.image
    // <>
    //     <div class="alert alert-danger alert-dismissible fade show" role="alert">Przepraszamy za utrudnienia nie udało się załadować danych.</div>
    // </>
    return (
        <section className="">
            {(status === 200) ?
                <>
                    <h1 className="m-4 border-bottom display-4" >O mnie </h1>
                    <div>
                        <p className="m-4">
                            <img id="media-query-float-left" src={image} className="rounded" alt="My image" />
                            {body.text}
                        </p>
                        <div className="end-of-float"></div>
                    </div>

                </>
                :
                <>
                    <div style={{ height: "300px" }}></div>
                </>
            }
        </section>
    );
}

export default AboutMeComponent;
