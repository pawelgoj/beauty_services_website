import React, { Component }  from 'react';



function PriceListComponent({ status, data}) {
    console.log(status);
    console.log(data);
    
    return (
        (status === 200) ?<>
        <h1 className="display-4 m-4">Cennik</h1>
        <div className="col-md-6 m-4">
            <table className="table table-striped my-2">
                <thead>
                    <tr>
                        <th scope="col">Nazwa usługi</th>
                        <th scope="col">Cena</th>
                    </tr>
                </thead>
                {data.map((item) => 
                <tbody>
                    <tr>
                        <th scope="row">{item.name}</th>
                        <td>{item.price + " zł"}</td>
                    </tr>
                </tbody>
                )}
            </table>
        </div>
        </> 
        : <></>
    );
}

export default PriceListComponent;