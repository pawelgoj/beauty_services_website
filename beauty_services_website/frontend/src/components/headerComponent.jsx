import React, { Component }  from 'react';

// Names of components must be written using capital letter.
function HeaderOfApp(prop) {
    return (
    <header>
        <div className="container-fluid m-0 p-0">
                <div id="headerCarousel" className="carousel slide" data-bs-ride="carousel">
                    <div className="carousel-indicators">
                        <button type="button" data-bs-target="#headerCarousel" data-bs-slide-to="0" className="active"
                            aria-label="Slide 1" aria-current="true"></button>
                        <button type="button" data-bs-target="#headerCarousel" data-bs-slide-to="1" aria-label="Slide 2"></button>
                    </div>
                    <div className="carousel-inner">
                        <div className="carousel-item active">
                            <img className="d-block w-100" src="./Baner.png" alt="ban"></img>
                        </div>
                        <div className="carousel-item">
                            <img className="d-block w-100" src="./BANER2.png" alt="ban2"></img>
                        </div>
                    </div>
                    <button className="carousel-control-prev" data-bs-target="#headerCarousel" type="button" data-bs-slide="prev">
                        <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span className="visually-hidden">Previous</span>
                    </button>
                    <button className="carousel-control-next" data-bs-target="#headerCarousel" type="button" data-bs-slide="next">
                        <span className="carousel-control-next-icon" aria-hidden="true"></span>
                        <span className="visually-hidden">Next</span>
                    </button>
                </div>
            </div>
        </header>
    );
}

export default HeaderOfApp;
