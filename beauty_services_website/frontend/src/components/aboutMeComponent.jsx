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
                    <h1 className="m-4 border-bottom" >O mnie </h1>
                    <img className="m-4" src={image} alt="My image" ></img>
                    <p className="m-4"> {body.text} </p>
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
