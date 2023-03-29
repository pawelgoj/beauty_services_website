import React, { useState, useEffect } from 'react';
import BlogComponent from '../components/blogComponent';

// Names of components must be written using capital letter.
const BLOG_URL = "/api/posts?quantity=4"


const BlogContainer = () => {
    const [posts, setState] = useState({ data: [] });
    const fetchData = () => {
        fetch(BLOG_URL, { method: "GET" })
            .then(res => {
                res.json().then(data => {
                    setState({
                        status: res.status,
                        data: data.results
                    });
                })
            }).catch(err => { setState(err) });
    }
    useEffect(fetchData, []);

    return (
        <BlogComponent posts={posts.data} />
    );
};


export default BlogContainer;