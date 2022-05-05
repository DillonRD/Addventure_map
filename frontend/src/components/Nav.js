import React from 'react';
import {Link} from "react-router-dom";

const Nav = (props) => {

    const logout = async () => {
        await fetch('http://127.0.0.1:8000/LoginAPI/logout', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            credentials: 'include',
        });

        props.setId('');
    }

    let navbarMenu;

    if ((props.id === '' || props.id === undefined)){
        navbarMenu = ( 
            <ul className="navbar mb-md-0">
                <li className="nav-item">
                    <Link to="/login" className="navbar-brand">Login</Link>
                </li>
                <li className="nav-item">
                    <Link to="/register" className="navbar-brand">Register</Link>
                </li>
            </ul>
        )
    
    }else {
        navbarMenu = (
            <ul className="navbar-nav mb-md-0">
                <li className="nav-item">
                    <Link to="/UpdateUser" className="navbar-brand">Profile</Link>
                </li>
                <li className="nav-item">
                    <Link to="/login" className="navbar-brand" onClick={logout} >Logout</Link>
                </li>
            </ul>
        )
    }

    return (
        <nav className="navbar navbar-expand-md navbar-dark bg-dark ">
            <div className="container-fluid">
                 <Link to="/" className="navbar-brand">Addventure<span role="img" aria-label="mountain">🗻</span></Link>
                 
                <div>
                    {navbarMenu}
                </div>
            </div>
        </nav>
    );
};

export default Nav;