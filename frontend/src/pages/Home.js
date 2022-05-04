import React, {useEffect, useState, Component} from 'react';
import {Navigate} from "react-router-dom";
import { GoogleMap, LoadScript, useLoadScript, Marker, InfoWindow, DirectionsRenderer } from '@react-google-maps/api';
import mapStyles from '../components/mapStyles.js';



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


/*
  lat 29.62218740747097, lng -98.57229513414572 
  lat 29.538541822605993, lng -98.75131433427904
  lat 29.56083169547403, lng -98.63034797249237
*/

function post(selected){
  
  var p = document.getElementById('post')
  p.innerHTML="";
  
  for(var i =0; i < (selected.location_post).length; i++){
    var temp = "<img src'"+selected.location_post[i].photo+"'><br><p>"+selected.location_post[i].likes+"<br>"+selected.location_post[i].text+"</p>"
    p.innerHTML.concat('<br>', temp)
  }
}

function review(selected){
  
  var r = document.getElementById('review')
  r.innerHTML="";
  
  for(var i =0; i < (selected.location_review).length; i++){
    var temp = "<img src'"+selected.location_review[i].photo+"'><br><p>"+selected.location_post[i].likes+"<br>"+selected.location_post[i].text+"</p>"
    r.innerHTML.concat('<br>', temp)
  }
}

function getReviews(user) {

    try {
        const response = await fetch('http://127.0.0.1:8000/adventure-map/review/' + user,{
            headers: {'Content-Type': 'application/json'},
            credentials: 'include'
        });
        setReviews(await response.json());
    } catch(error) {
        return [];
    }

}

function getPosts(user) {

    try {
        const response = await fetch('http://127.0.0.1:8000/adventure-map/post/' + user,{
            headers: {'Content-Type': 'application/json'},
            credentials: 'include'
        });
        setPosts(await response.json());
    } catch(error) {
        return [];
    }

}


const Home = (props) => {

  const [content, setContent] = useState([]);
  const [loc, setPos]= useState();
  const [selected, setSelected] = useState(null);
  const [directions, setDirections] = useState();
  const [reviews, setReviews] = useState([]);
  const [posts, setPosts] = useState([]);

  const mapRef = React.useRef();
  const onMapLoad = React.useCallback((map) =>{
    mapRef.current = map;
  }, []);

  const {isLoaded, loadError} = useLoadScript({
      googleMapsApiKey:process.env.REACT_APP_GOOGLE_MAPS_API_KEY,
      libraries,
    });
    
  useEffect(() => {
    (
        async () => {
            const response = await fetch('http://127.0.0.1:8000/location/all', {
                headers: {'Content-Type': 'application/json'},
                credentials: 'include',
            });
            
            setContent(await response.json());
            
        }
    )();
    }, []);
    
    const fetchLoc = () =>{
      
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            
            const pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude,
            };
            setPos(pos)
          },
          () => {
            alert("Error Please allow location refresh and try again")
          }
        );
      } else {
        // Browser doesn't support Geolocation
        alert("Error Please allow location refresh and try again")
      }
      
    }
    const fetchDirections = event =>{
      
      const service = new window.google.maps.DirectionsService();
        service.route({
          origin: loc,
          destination: {lat: parseFloat(selected.lat), lng: parseFloat(selected.lng)},
          travelMode : window.google.maps.TravelMode.DRIVING
        },
        (result, status) =>{
          if(status==="OK" && result){
            setDirections(result);
            return false;
          }
          return false;
        }
        
        );
    }
    if (loadError) return "Error loading maps";
    if(!isLoaded) return "Loadin Maps";
    
    console.log(content)
    
    return (     
      <div> 
      <GoogleMap 
      mapContainerStyle={containerStyle}
      zoom={10}
      center={center}
      options={options}
      onLoad={onMapLoad}
      >
      {content.map(content => (
        <Marker
        key={parseInt(content.id)}
        position={{lat: parseFloat(content.lat), lng: parseFloat(content.lng)}}
        onClick={() => {
          setSelected(content);
          fetchLoc()
        }}
        />
      ))}
      {directions && <DirectionsRenderer directions={directions}/>}
      {selected ? (
      <InfoWindow
        position={{lat: parseFloat(selected.lat), lng: parseFloat(selected.lng)}}
        onCloseClick={()=> {
          setSelected(null);
          setDirections(null);
        }}
        >
        <div >
          <p className="p-2 bold lead text-center text-break text-wrap" style={{width: "15rem"}}>
            <b>{selected.name}</b>
          </p>
          <p className="p-2 bold lead text-center text-break text-wrap" style={{width: "15rem"}}>
            {selected.description}
          </p>
          <div className="p-2 d-grid gap-2">
            <button className="btn btn-success" type="button" onClick={fetchDirections}>Directions</button>
          </div>
          <div className="p-2 btn-group m-5" role="group" aria-label="Basic radio toggle button group">
            <input type="radio" className="btn-check" name="btnradio" id="btnradio1" autoComplete="off" ></input>
            <label className="btn btn-outline-success" htmlFor="btnradio1" >Post</label>
            {posts.map(post => (
              <label>{post.text}, Likes: {post.likes}</label>
            ))}
            <input type="radio" className="btn-check" name="btnradio" id="btnradio2" autoComplete="off" ></input>
            <label className="btn btn-outline-success" htmlFor="btnradio2">Reviews</label>
            {reviews.map(review => (
              <label>{review.text}, Rating: {review.rating}</label>
            ))}
          </div>
          <div id="post">

          </div>
        </div>
      </InfoWindow>) : null}
      </GoogleMap>
      </div>
      
    )
};

export default Home;