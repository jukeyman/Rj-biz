exports.handler = async (event, context) => {
  if (event.httpMethod !== 'POST') {
    return {
      statusCode: 405,
      body: 'Method Not Allowed'
    }
  }

  try {
    const data = JSON.parse(event.body)
    
    // Here you can add additional processing like sending emails
    // For now, we'll just return success
    
    return {
      statusCode: 200,
      body: JSON.stringify({
        message: 'Form submission successful',
        data: data
      })
    }
  } catch (error) {
    return {
      statusCode: 400,
      body: JSON.stringify({
        message: 'Invalid request',
        error: error.message
      })
    }
  }
} 