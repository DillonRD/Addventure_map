import React from 'react';
import ReactDOM from 'react-dom';

function CreateUserForm(props) {
  return (
    <form>
      <label>User Name:
        <input type="text" value={username} />
      </label>
	<label>Password:
        <input type="password" value={password} />
      </label>
	<label>First Name:
        <input type="text" value={firstname} />
      </label>
	<label>Last Name:
        <input type="text" value={lastname} />
      </label>
	<label>Date of Birth:
        <input type="date" value={dateOfBirth} />
      </label>
	<label>Phone:
        <input type="text" value={phone} />
      </label>
	<label>Email:
        <input type="text" value={email} />
      </label>
	<label>Address:
        <input type="text" value={address} />
      </label>
	<label>City:
        <input type="text" value={city} />
      </label>
	<label>ZIP Code:
        <input type="text" value={zipcode} />
      </label>
	<label>Latitude:
        <input type="text" value={latitude} />
      </label>
	<label>Longitude:
        <input type="text" value={longitude} />
      </label>
    </form>
  )
}

function UpdateUserForm(props) {
  return (
    <form>
      <label>User Name:
        <input type="text" value={username} />
      </label>
	<label>Password:
        <input type="password" value={password} />
      </label>
	<label>First Name:
        <input type="text" value={firstname} />
      </label>
	<label>Last Name:
        <input type="text" value={lastname} />
      </label>
	<label>Date of Birth:
        <input type="date" value={dateOfBirth} />
      </label>
	<label>Phone:
        <input type="text" value={phone} />
      </label>
	<label>Email:
        <input type="text" value={email} />
      </label>
	<label>Address:
        <input type="text" value={address} />
      </label>
	<label>City:
        <input type="text" value={city} />
      </label>
	<label>ZIP Code:
        <input type="text" value={zipcode} />
      </label>
	<label>Latitude:
        <input type="text" value={latitude} />
      </label>
	<label>Longitude:
        <input type="text" value={longitude} />
      </label>
    </form>
  )
}

//ReactDOM.render(<CreateUserForm />, document.getElementById('root'));