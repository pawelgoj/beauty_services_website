import React, { Component } from 'react';
import './css/App.css';
import HeaderComponent from './components/headerComponent';
import NavBarComponent from './components/navBarComponent';
import ContactComponent from './components/contactComponent';
import CalendarComponent from './components/calendarComponent';
import BlogComponent from './components/myBlogComponent';
import ServicesComponent from './components/servicesComponent';

import AboutMeContainer from './containers/aboutMeContainer';
import FooterContainer from './containers/footerContainer';
import PriceListContainer from './containers/priceListContainer';


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
      <BlogComponent />
      <FooterContainer />

    </>
  );
}

export default App;
