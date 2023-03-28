import React, { Component } from 'react';


// Names of components must be written using capital letter.
function AboutMeComponent({ status, body }) {
    let image = "data:image/png;base64," + body.image
    // <>
    //     <div class="alert alert-danger alert-dismissible fade show" role="alert">Przepraszamy za utrudnienia nie udało się załadować danych.</div>
    // </>
    return (
        <section>
            {(status === 200) ?
                <>
                    <h1 className="m-4 border-bottom display-4" >O mnie </h1>
                    <div >
                        <img style={{ float: "left", clear: "left"}} src={image} alt="My image" />
                        <p className="m-4">{body.text}</p>
                        <div style={{ clear: "left"}}/>
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
