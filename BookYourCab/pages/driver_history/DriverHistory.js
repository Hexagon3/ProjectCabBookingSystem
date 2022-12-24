import { StyleSheet, Text, Button, View } from 'react-native';
import { React } from 'react';
// import history_data from './temp/data';


var history_data = [
  {
      id:5620,
      source:"Barabazar",
      destination:"Chadnichak",
      distance:512,
      price: 620,
      start_time:"10:42am",
      end_time:"11:15am",
      n_traveller:2
  },
  {
      id:6565,
      source:"Barabazar",
      destination:"Chadnichak",
      distance:512,
      price: 620,
      start_time:"10:42am",
      end_time:"11:15am",
      n_traveller:2
  }]



function ListItem({item}){
  return (
    <View style={styleList.historyBox}>

      <Text> Order ID: {item.id}</Text>
      <View>
        <Text>{item.source}</Text><View style={styleList.initDot}/>
      </View>
    </View>
    ) 
}


export default function ListView() {
    return (
    <>
    <ListItem item={history_data[1]} />
    </>
          
      );
}






const styleList = StyleSheet.create({
  historyBox: {
    // display:'block',
    
    width:'95%',
    borderRadius:15,
    borderColor:"#2F2058",
    borderWidth:3,
    backgroundColor: '#73D5FF',
    // alignItems: 'center',
    // justifyContent: 'center',
    margin:5
  },
  initDot:{
    /* Ellipse 7 */

      width: 20,
      height: 20,  
      background: "#FFB800",
      borderRadius:20,
      borderWidth:4

  }
});


