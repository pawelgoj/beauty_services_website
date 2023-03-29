import React, { Component } from 'react';
import './css/App.css';
import HeaderComponent from './components/headerComponent';
import NavBarComponent from './components/navBarComponent';
import ContactComponent from './components/contactComponent';
import CalendarComponent from './components/calendarComponent';
import ServicesComponent from './components/servicesComponent';

import AboutMeContainer from './containers/aboutMeContainer';
import FooterContainer from './containers/footerContainer';
import PriceListContainer from './containers/priceListContainer';
import BlogContainer from './containers/blogContainer';


function App() {
  return (
    <>
      <HeaderComponent />
      <NavBarComponent />
      <AboutMeContainer />
      <ServicesComponent />
      <PriceListContainer />
      <CalendarComponent />
      <ContactComponent />
      <BlogContainer />
      <FooterContainer />

    </>
  );
}

export default App;
