import { useState } from "react"
import { useNavigate } from "react-router-dom"
import { useParams } from "react-router-dom"


export default function Edit(props){
   
    const {name} = useParams();
    const [editData,setEditData] = useState(props.users.filter((user)=>user.name == name)[0])
   const navigate=useNavigate()
    const edit =()=>{
        let existingUserData=props.users;
        let newUserData=[]
        existingUserData.forEach((user)=>{
           
            if (user.name==name){
                newUserData.push(editData)
               
            }
            else{
                newUserData.push(user)
            }
            navigate("/users")
        })
        props.setUsers(newUserData)
    }



    return (
        <>
        
        <h1>Edit Page</h1>
        {JSON.stringify(editData)}
        <div className="form">
            <div className="form-input">
                <label>Name:</label>
                <input type="text" defaultValue={props.users.filter((user)=>user.name==name)[0].name} onKeyUp={(e)=>setEditData({
                        ...editData,
                        name:e.target.value

                })}></input>
            </div>
            <div className="form-input">
                <label>Email:</label>
                <input type="email" defaultValue={props.users.filter((user)=>user.name==name)[0].email} onKeyUp={(e)=>setEditData({
                        ...editData,
                        email:e.target.value

                })}></input>
            </div>
            <div className="form-input">
                <label>Password:</label>
                <input type="text"  onKeyUp={(e)=>setEditData({
                        ...editData,
                        password:e.target.value

                })}></input>
            </div>
            <div className="form-input">
                <button type="button" onClick={edit} >update user</button>
            </div>
        </div>
        </>
    )
}