import React, { Component } from 'react';
import './css/App.css';
import HeaderComponent from './components/headerComponent';
import FooterComponent from './components/footerComponent';
import AboutMeComponent from './components/aboutMeComponent';
import NavBarComponent from './components/navBarComponent';
import ContactComponent from './components/contactComponent';
import CalendarComponent from './components/calendarComponent';
import BlogComponent from './components/myBlogComponent';
import PriceListComponent from './components/priceListComponent';
import ServicesComponent from './components/servicesComponent';
import AboutMeContainer from './containers/aboutMeContainer';


function App() {
  return (
    <>
      <HeaderComponent />
      <NavBarComponent />
      <AboutMeContainer />
      <ServicesComponent />
      <PriceListComponent />
      <CalendarComponent />
      <ContactComponent />
      <BlogComponent />
      <FooterComponent />

    </>
  );
}

export default App;
