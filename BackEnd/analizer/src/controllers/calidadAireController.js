import { fetchWeatherApi } from 'openmeteo';

export const obtenerCalidadDeAire = async (req, res) => {


  const params = {
    "latitude": 52.52,
    "longitude": 13.41,
    
  };
  const url = "https://air-quality-api.open-meteo.com/v1/air-quality";
  const responses = await fetchWeatherApi(url, params);
  
  // Process first location. Add a for-loop for multiple locations or weather models
  const response = responses[0];
  
  // Attributes for timezone and location
  const utcOffsetSeconds = response.utcOffsetSeconds();
  const timezone = response.timezone();
  const timezoneAbbreviation = response.timezoneAbbreviation();
  const latitude = response.latitude();
  const longitude = response.longitude();

  res.json({
    ciudad: 'Ciudad de Guatemala',
    timezone: timezone,
    timezoneAbbreviation: timezoneAbbreviation,
    utcOffsetSeconds: utcOffsetSeconds,
    fecha_hora: response.timezoneAbbreviation(),
    latitud: latitude,
    longitud: longitude,
    calidad_aire: responses

  });
};
