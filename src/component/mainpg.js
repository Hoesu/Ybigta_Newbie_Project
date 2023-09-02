// import React from "react";
// import Container from '@mui/material/Container';
// import { Stack, Box, Typography, FormGroup } from "@mui/material";
// import { styled } from '@mui/material/styles';
// import FormControlLabel from '@mui/material/FormControlLabel';
// import Switch from '@mui/material/Switch';
// import Paper from '@mui/material/Paper';
// import Grid from '@mui/material/Grid';

// const Mainpg = () =>  {


//     const AntSwitch = styled(Switch)(({ theme }) => ({
//         width: 32,
//         height: 20,
//         padding: 0,
//         display: 'flex',
//         '&:active': {
//           '& .MuiSwitch-thumb': {
//             width: 15,
//           },
//           '& .MuiSwitch-switchBase.Mui-checked': {
//             transform: 'translateX(9px)',
//           },
//         },
//         '& .MuiSwitch-switchBase': {
//           padding: 2,
//           '&.Mui-checked': {
//             transform: 'translateX(12px)',
//             color: '#fff',
//             '& + .MuiSwitch-track': {
//               opacity: 1,
//               backgroundColor: theme.palette.mode === 'dark' ? '#177ddc' : '#1890ff',
//             },
//           },
//         },
//         '& .MuiSwitch-thumb': {
//           boxShadow: '0 2px 4px 0 rgb(0 35 11 / 20%)',
//           width: 16,
//           height: 16,
//           borderRadius: 10,
//           transition: theme.transitions.create(['width'], {
//             duration: 200,
//           }),
//         },
//         '& .MuiSwitch-track': {
//           borderRadius: 20 / 2,
//           opacity: 1,
//           backgroundColor:
//             theme.palette.mode === 'dark' ? 'rgba(255,255,255,.35)' : 'rgba(0,0,0,.25)',
//           boxSizing: 'border-box',
//         },
//       }));
      

//     // ----------------------------------------------------------

//     return(
//         <Container maxWidth
//         sx={{bgcolor: 'white',
//         display: 'flex',
//         alignItems: 'center',
//         justifyContent: 'center',
//         flexDirection: 'column',
//         }}>
        

//         <Box
//         sx={{ 
//             pt: 2,
//             width: "100%", height: '200px'}}
//         >

        

//         <Stack spacing={2} direction='row' 
//         justifyContent='center' >

    

//         <Box border="1px solid #000"
//         sx={{ bgcolor: 'white',
//             width:'100%', height: '200px'
            
//         }}
//         >

//         <Typography>
//             box 1
//         </Typography>
//         </Box>

//         <Box
//         sx={{ bgcolor: 'white',
//             width:'100%', height: '200px',
//             boxShadow: 3
//         }}
//         >

//         <Typography>
//             box 2
//         </Typography>
//         </Box>

//         <Box
//         sx={{ bgcolor: 'white',
//             width:'100%', height: '200px',
//             boxShadow: 2
//         }}
//         >

//         <Typography>
//             box 3
//         </Typography>
//         </Box>

//         <Box
//         sx={{ bgcolor: 'white',
//             width:'100%', height: '200px',
//             boxShadow: 2
//         }}
//         >

//         <Typography>
//             box 4
//         </Typography>
//         </Box>

//         <Box
//         sx={{ bgcolor: 'yellow',
//             width:'100%', height: 'auto'}}
//         >

//         <Typography>
//             box 5
//         </Typography>
//         </Box>
//         {/* </Grid> */}

//         </Stack>

        

//        </Box>

//        <Stack sx={{pt: 2, pb: 2
//     }}>

//         <Box
//         sx={{ bgcolor: 'lightgrey',
//         width:'100%', height: 'auto',
//         display: 'flex',
//         alignItems: 'center',
//         justifyContent: 'center',
//         flexDirection: 'column',
//     }}
//     >

//         <Typography>
//             욕설 클린봇 켜기/끄기
//         </Typography>


//         <FormGroup>
//         <Stack direction="row" spacing={1} alignItems="center">
//         <Typography>Off</Typography>
//         <AntSwitch defaultChecked inputProps={{ 'aria-label': 'ant design' }} />
//         <Typography>On</Typography>
//       </Stack>
//         </FormGroup>


//         </Box>
//         </Stack>

//         </Container>
//     );
// };

// export default Mainpg;