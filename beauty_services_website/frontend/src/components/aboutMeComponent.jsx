import React, { Component }  from 'react';


// Names of components must be written using capital letter.
function AboutMeComponent({status, body}) {
    console.log(status)
    let image = "data:image/png;base64," + body.image
    // <>
    //     <div class="alert alert-danger alert-dismissible fade show" role="alert">Przepraszamy za utrudnienia nie udało się załadować danych.</div>
    // </>
    return (
        <section>
            {(status === 200) ? 
            <>
                <h1>O mnie </h1>
                <img src= {image} alt="My image" ></img>
                <p> {body.text} </p>
            </>
            : 
            <>
                <div></div>
            </>
            }
        </section>
    );
}

export default AboutMeComponent;
