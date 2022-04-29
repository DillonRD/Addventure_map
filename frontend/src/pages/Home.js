import React, {useEffect, useState, Component} from 'react';
import { GoogleMap, LoadScript, useJsApiLoader } from '@react-google-maps/api';
import mapStyles from '../components/mapStyles.js';
import { Marker } from '@react-google-maps/api';


const containerStyle = {
    width: '100vw',
    height: '100vh',
  };
  
const center = {
    lat: 29.4252,
    lng: -98.4946,
  };
const libraries = ["places"]; 
  
  
const options = {
styles: mapStyles,
disableDefaultUI: true,
zoomControl:true,
minZoom:4,
maxZoom: 18,
};



const Home = (props) => {

    const {isLoaded, loadError} = useJsApiLoader({
        googleMapsApiKey:process.env.REACT_APP_GOOGLE_MAPS_API_KEY,
        libraries,
      });
    
      const [markers, setMarkers] = React.useState([]);
      
      

      if (loadError) return "Error loading maps";
      if(!isLoaded) return "Loadin Maps";
      
      return (        
        <GoogleMap mapContainerStyle={containerStyle}
        zoom={10}
        center={center}
        options={options}
        onClick={(event)=>{
            setMarkers(current => [
              ...current,
              {
              lat:event.latLng.lat(),
              lng:event.latLng.lng(),
            },
          ]);
        }}
        ></GoogleMap>
      )
};

export default Home;