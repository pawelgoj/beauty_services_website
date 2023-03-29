import React, { useState, useEffect } from 'react';
import PriceListComponent from '../components/priceListComponent';

// Names of components must be written using capital letter.
const ABOUT_ME_URL = "/business/price_list"


const PriceListContainer = () => {
    const [priceList, setState] = useState({ status: "", body: "" });
    const fetchData = () => {
        fetch(ABOUT_ME_URL, { method: "GET" })
            .then(res => {
                res.json().then(data => {
                    setState({ status: res.status, body: data.results });
                })
            })
            .catch(err => { setState(err) });
    }
    useEffect(fetchData, []);

    return (
        <PriceListComponent status={priceList.status} data={priceList.body} />
    );
};


export default PriceListContainer;