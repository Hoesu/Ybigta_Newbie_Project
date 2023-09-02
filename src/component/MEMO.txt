import PropTypes from 'prop-types';
import { useTheme, styled } from '@mui/material/styles';
import AppBar from '@mui/material/AppBar';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import { Stack, Box, Typography, FormGroup } from "@mui/material";
import Container from '@mui/material/Container';
import Switch from '@mui/material/Switch';
import { collection, getDoc, doc } from "firebase/firestore"; 
import { dbService } from "../firebaseSDK";
import React, { useState, useEffect } from "react";


function TabPanel(props) {
    const { children, value, index, ...other } = props;
  
    return (


      <div
        role="tabpanel"
        hidden={value !== index}
        id={`full-width-tabpanel-${index}`}
        aria-labelledby={`full-width-tab-${index}`}
        {...other}
      >
        {value === index && (
          <Box sx={{ p: 3 }}>
            <Typography>{children}</Typography>
          </Box>
        )}
      </div>
    );
  }
  
  TabPanel.propTypes = {
    children: PropTypes.node,
    index: PropTypes.number.isRequired,
    value: PropTypes.number.isRequired,
  };
  
  function a11yProps(index) {
    return {
      id: `full-width-tab-${index}`,
      'aria-controls': `full-width-tabpanel-${index}`,
    };
  }


// ------------------------------------------------------


const Tabpg = () => {
    const theme = useTheme();
    const [value, setValue] = React.useState(0);
    const [gameData, setGameData] = useState([null]);
    const [gameData1, setGameData1] = useState([null]);
    const [gameData2, setGameData2] = useState([null]);
    const [gameData3, setGameData3] = useState([null]);
    const [gameData4, setGameData4] = useState([null]);


    const handleChange = (event, newValue) => {
        setValue(newValue);
      };
    
      const handleChangeIndex = (index) => {
        setValue(index);
      };


      const fetchGameData = async () => {
    try {
      const docRef = doc(dbService, "all_game_comments", "87b2bPNwgEYr3tSnK8gp");
      const docSnapshot = await getDoc(docRef);

      if (docSnapshot.exists()) {
        setGameData(docSnapshot.data());
      } else {
        console.log("No such document!");
      }
    } catch (error) {
      console.error("Error fetching document:", error);
    }
  };

  useEffect(() => {
    fetchGameData();
  }, []);


  const fetchGameData1 = async () => {
    try {
      const docRef = doc(dbService, "all_game_comments", "A3cyyE4vlziMiNDJBRCx");
      const docSnapshot = await getDoc(docRef);

      if (docSnapshot.exists()) {
        setGameData1(docSnapshot.data());
      } else {
        console.log("No such document!");
      }
    } catch (error) {
      console.error("Error fetching document:", error);
    }
  };

  useEffect(() => {
    fetchGameData1();
  }, []);


  const fetchGameData2 = async () => {
    try {
      const docRef = doc(dbService, "all_game_comments", "V1HZrIjihuHmUwMsDwc8");
      const docSnapshot = await getDoc(docRef);

      if (docSnapshot.exists()) {
        setGameData2(docSnapshot.data());
      } else {
        console.log("No such document!");
      }
    } catch (error) {
      console.error("Error fetching document:", error);
    }
  };

  useEffect(() => {
    fetchGameData2();
  }, []);


  const fetchGameData3 = async () => {
    try {
      const docRef = doc(dbService, "all_game_comments", "dTq1yQ06HH3aU6dgRs0L");
      const docSnapshot = await getDoc(docRef);

      if (docSnapshot.exists()) {
        setGameData3(docSnapshot.data());
      } else {
        console.log("No such document!");
      }
    } catch (error) {
      console.error("Error fetching document:", error);
    }
  };

  useEffect(() => {
    fetchGameData3();
  }, []);


  const fetchGameData4 = async () => {
    try {
      const docRef = doc(dbService, "all_game_comments", "gcOP6cZUKRAkC3e8FnGq");
      const docSnapshot = await getDoc(docRef);

      if (docSnapshot.exists()) {
        setGameData4(docSnapshot.data());
      } else {
        console.log("No such document!");
      }
    } catch (error) {
      console.error("Error fetching document:", error);
    }
  };

  useEffect(() => {
    fetchGameData4();
  }, []);



  
    


    // ----------------------------------------------------------------
    //on/off 기능

    const AntSwitch = styled(Switch)(({ theme }) => ({
        width: 32,
        height: 20,
        padding: 0,
        display: 'flex',
        '&:active': {
          '& .MuiSwitch-thumb': {
            width: 15,
          },
          '& .MuiSwitch-switchBase.Mui-checked': {
            transform: 'translateX(9px)',
          },
        },
        '& .MuiSwitch-switchBase': {
          padding: 2,
          '&.Mui-checked': {
            transform: 'translateX(12px)',
            color: '#fff',
            '& + .MuiSwitch-track': {
              opacity: 1,
              backgroundColor: theme.palette.mode === 'dark' ? '#177ddc' : '#1890ff',
            },
          },
        },
        '& .MuiSwitch-thumb': {
          boxShadow: '0 2px 4px 0 rgb(0 35 11 / 20%)',
          width: 16,
          height: 16,
          borderRadius: 10,
          transition: theme.transitions.create(['width'], {
            duration: 200,
          }),
        },
        '& .MuiSwitch-track': {
          borderRadius: 20 / 2,
          opacity: 1,
          backgroundColor:
            theme.palette.mode === 'dark' ? 'rgba(255,255,255,.35)' : 'rgba(0,0,0,.25)',
          boxSizing: 'border-box',
        },
      }));

      // -----------------------------------------------------------------



    return(
        <Container 
        sx={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        flexDirection: 'column',
        }}>

        <Box sx={{ bgcolor: 'background.paper', width:'100%', height: 'auto' }}>

      <AppBar position="static">
        <Tabs
          value={value}
          onChange={handleChange}
          indicatorColor="secondary"
          textColor="inherit"
          variant="fullWidth"
          aria-label="full width tabs example"
        >
          <Tab label="리그오브레전드" {...a11yProps(0)} />
          <Tab label="메이플스토리" {...a11yProps(1)} />
          <Tab label="피파온라인 4" {...a11yProps(2)} />
          <Tab label="디아블로 4" {...a11yProps(3)} />
          <Tab label="로스트아크" {...a11yProps(4)} />
        </Tabs>
      </AppBar>
      
        <TabPanel value={value} index={0} >
          리그오브레전드 게시판

          <ul>
      {gameData4 && gameData4.leagueoflegends && Object.keys(gameData4.leagueoflegends).map((key) => (
        <li key={key}>
          {key}: {gameData4.leagueoflegends[key]}
        </li>
      ))}
      </ul>  
        </TabPanel>
        <TabPanel value={value} index={1} >
          메이플스토리 게시판

          <ul>
      {gameData && gameData.maplestory && Object.keys(gameData.maplestory).map((key) => (
        <li key={key}>
          {key}: {gameData.maplestory[key]}
        </li>
      ))}
      </ul>
        </TabPanel>
        <TabPanel value={value} index={2} >
          피파온라인 4 게시판

          <ul>
      {gameData3 && gameData3.fifa4 && Object.keys(gameData3.fifa4).map((key) => (
        <li key={key}>
          {key}: {gameData3.fifa4[key]}
        </li>
      ))}
      </ul>  
        </TabPanel>
        <TabPanel value={value} index={3} >
          디아블로 4 게시판

          <ul>
      {gameData2 && gameData2.diablo4 && Object.keys(gameData2.diablo4).map((key) => (
        <li key={key}>
          {key}: {gameData2.diablo4[key]}
        </li>
      ))}
      </ul>  
        </TabPanel>
        <TabPanel value={value} index={4} >
          로스트아크 게시판

          <ul>
      {gameData1 && gameData1.lostark && Object.keys(gameData1.lostark).map((key) => (
        <li key={key}>
          {key}: {gameData1.lostark[key]}
        </li>
      ))}
      </ul>          
        </TabPanel>
      
    </Box>


    <Stack sx={{pt: 2, pb: 2
    }}>

        <Box
        sx={{ 
        width:'100%', height: 'auto',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        flexDirection: 'column',
        pt: 2,
        pb: 2
    }}
    >

        <Typography>
            욕설 클린봇 켜기/끄기
        </Typography>


        <FormGroup>
        <Stack direction="row" spacing={1} alignItems="center">
        <Typography>Off</Typography>
        <AntSwitch defaultChecked inputProps={{ 'aria-label': 'ant design' }} />
        <Typography>On</Typography>
      </Stack>
        </FormGroup>


        </Box>
        </Stack>


    </Container>


    );
}

export default Tabpg;