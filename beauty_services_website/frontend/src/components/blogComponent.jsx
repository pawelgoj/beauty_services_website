import React, { Component } from 'react';

// TODO

function BlogComponent({ posts }) {
    return (
        <>
            <div>
                <h1 className="display-6 m-4">Zapraszam również na mój blog</h1>
                <p className="mx-4">Znajdziesz tam ciekawe artykuły na temat kosmetologii:&nbsp;
                    <a href=''>Link do bloga</a>
                </p>
            </div>
            <div className="mx-4 mt-2 mb-5">
                <h2 className="h4">O to niektóre artykuły:</h2>
                <div className="row row-cols-1 row-cols-md-2 g-4">
                    {posts.map((item) => (
                        <div className="col">
                            <div className="card">
                                <div className="row g-0">
                                    <div class="col-md-4">
                                        {/* TODO */}
                                        <img id="bootstrap-overrides-image-hover" src={item.images[0].url} alt={item.title} className="bd-placeholder-img" width="100%" role="img" aria-label="Placeholder: Image" preserveAspectRatio="xMidYMid slice" focusable="false" />

                                        <rect width="100%" height="100%" fill="#868e96"></rect>
                                    </div>
                                    <div className="col-md-8">
                                        <div class="card-body">
                                            <h5 class="card-title">{item.title}</h5>
                                            <p class="card-text">{item.content}</p>
                                            <p class="card-text">
                                                <small class="text-muted">{item.date}</small>
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </>
    );
}

export default BlogComponent;