import React, {useEffect, useState, Component} from 'react';
import {Link, Navigate} from "react-router-dom";
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

const Home = (props) => {

  const [content, setContent] = useState([]);
  const [loc, setPos]= useState();
  const [selected, setSelected] = useState(null);
  const [directions, setDirections] = useState();

  const [reviews, setReviews] = useState([]);
  const [posts, setPosts] = useState([]);
  const [activities, setActivities] = useState([]);

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

    const fetchActivities = async (e) => {
        const response = await fetch('http://127.0.0.1:8000/activity/name=' + selected.name,{
            headers: {'Content-Type': 'application/json'},
            credentials: 'include'
        });

        setActivities(await response.json());
        setReviews([]);
        setPosts([]);
    }

    const fetchReviews = async (e) => {
        const response = await fetch('http://127.0.0.1:8000/review/name=' + selected.name,{
            headers: {'Content-Type': 'application/json'},
            credentials: 'include'
        });

        setReviews(await response.json());
        setActivities([]);
        setPosts([]);
    }

    const fetchPosts = async (e) => {
        const response = await fetch('http://127.0.0.1:8000/post/name=' + selected.name,{
            headers: {'Content-Type': 'application/json'},
            credentials: 'include'
        });

        setPosts(await response.json());
        setActivities([]);
        setReviews([]);
    }
    
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
            setPosts([]);
            setActivities([]);
            setReviews([]);
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
          setPosts([]);
          setActivities([]);
          setReviews([]);
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

            <div className="btn-group" role="group" aria-label="Basic radio toggle button group" style={{width: "15rem"}}>
                <input type="radio" className="btn-check" name="btnradio" id="btnradio1" autoComplete="off"/>
                <label className="btn btn-outline-success" htmlFor="btnradio1" onClick={fetchPosts}>Posts</label>

                <input type="radio" className="btn-check" name="btnradio" id="btnradio2" autoComplete="off"/>
                <label className="btn btn-outline-success" htmlFor="btnradio2" onClick={fetchReviews}>Reviews</label>

                <input type="radio" className="btn-check" name="btnradio" id="btnradio3" autoComplete="off"/>
                <label className="btn btn-outline-success" htmlFor="btnradio3" onClick={fetchActivities}>Activities</label>
            </div>


            <div style={{width: "15rem", height: "5rem"}}>
                {activities.map(activity => (
                    <div>
                        Name: {activity.name}<br/>
                        Description: {activity.description}<br/>
                        Difficulty: {activity.difficulty}<br/>
                    </div>
                ))}

                {reviews.map(review => (
                    <div>
                        Comment: {review.text}<br/>
                        Rating: {review.rating}<br/>
                    </div>
                ))}

                {posts.map(post => (
                    <div>
                        Comment: {post.text}<br/>
                        Likes: {post.likes}<br/>
                    </div>
                ))}
            </div>
        </div>
      </InfoWindow>) : null}
      </GoogleMap>
      </div>
      
    )
};

export default Home;