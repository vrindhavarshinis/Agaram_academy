import { useState } from "react";
import { useNavigate } from "react-router-dom";
import './index.css'


export default function Create(props){

   
    const navigate=useNavigate();
    const [createData,setCreateData]=useState({
      name:"",
      email:"",
      password:""
    });

    

    const create =()=>{
        props.setUsers([...props.users,createData])
        navigate('/users')
    }
    

    
    
    return (
        <>
        
        <h1>Create Page</h1>
        {JSON.stringify(createData)}
        <div className="form">
            <div className="form-input">
                <label>Name:</label>
                <input type="text" onKeyUp={(e)=>setCreateData({
                        ...createData,
                        name:e.target.value

                })}></input>
            </div>
            <div className="form-input">
                <label>Email:</label>
                <input type="email"  onKeyUp={(e)=>setCreateData({
                        ...createData,
                        email:e.target.value

                })}></input>
            </div>
            <div className="form-input">
                <label>Password:</label>
                <input type="text"  onKeyUp={(e)=>setCreateData({
                        ...createData,
                        password:e.target.value

                })}></input>
            </div>
            <div className="form-input">
                <button type="button" onClick={()=>create()} >Create User</button>
            </div>
        </div>
        </>
    )
}