import { useParams } from "react-router-dom";

export default function View(props){
    console.log("propsusers",props.users)
    const {name} = useParams();
    
    return (
        <>
        <div>
            <h1>View Page</h1>
            <br/>
            <h2>{name}</h2>
            {
                console.log("propsusers",props.users[0].email)
            }
           

            <h2>{(props.users.filter((user)=>user.name===name)[0].email)}</h2>

            
        </div>
        


      

        {
            
        }
         </>
    )
}