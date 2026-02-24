document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const moodSelect = document.getElementById('mood');
    const cityInput = document.getElementById('city');
    const submitBtn = document.getElementById('submit-btn');
    const tryAgainBtn = document.getElementById('try-again-btn');
    const errorTryAgainBtn = document.getElementById('error-try-again-btn');
    const loadingSection = document.getElementById('loading');
    const resultSection = document.getElementById('result');
    const errorSection = document.getElementById('error');
    const errorMessage = document.getElementById('error-message');
    
    // Result elements
    const resultCity = document.getElementById('result-city');
    const weatherIcon = document.getElementById('weather-icon');
    const weatherDescription = document.getElementById('weather-description');
    const temperature = document.getElementById('temperature');
    const moodMatchText = document.getElementById('mood-match-text');
    const songTitle = document.getElementById('song-title');
    const songArtist = document.getElementById('song-artist');
    const songLink = document.getElementById('song-link');
    
    // API endpoint
    const apiUrl = '/recommend';
    
    // Event listeners
    submitBtn.addEventListener('click', handleSubmit);
    tryAgainBtn.addEventListener('click', resetForm);
    errorTryAgainBtn.addEventListener('click', resetForm);
    
    // Form submission handler
    async function handleSubmit() {
        const mood = moodSelect.value;
        const city = cityInput.value;
        
        // Validate inputs
        if (!city) {
            showError('Please enter your city.');
            return;
        }
        
        // Show loading state
        showLoading();
        
        try {
            const response = await fetch(apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ mood, city })
            });
            
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Failed to get recommendations');
            }
            
            const data = await response.json();
            displayResult(data);
        } catch (error) {
            showError(error.message);
        }
    }
    
    // Display the recommendation result
    function displayResult(data) {
        // Update city
        resultCity.textContent = data.city || data.location;
        
        // Update weather info
        weatherDescription.textContent = data.weather.description;
        temperature.textContent = data.weather.temperature;
        
        // Set weather icon based on conditions
        setWeatherIcon(data.weather.conditions);
        
        // Update mood match text
        if (data.mood_matches_weather) {
            moodMatchText.textContent = `Your ${data.mood} mood matches the current weather!`;
            moodMatchText.style.color = 'var(--success-color)';
        } else if (data.mood_matches_weather === false) {
            moodMatchText.textContent = `Your ${data.mood} mood doesn't quite match the current weather.`;
            moodMatchText.style.color = 'var(--text-color)';
        } else {
            // If mood_matches_weather is null (when mood is derived from weather)
            moodMatchText.textContent = `We've selected a ${data.mood} song based on the current weather.`;
            moodMatchText.style.color = 'var(--primary-color)';
        }
        
        // Update song recommendation
        songTitle.textContent = data.song_recommendation.title;
        songArtist.textContent = data.song_recommendation.artist;
        songLink.href = data.song_recommendation.url;
        
        // Hide loading, show result
        hideLoading();
        resultSection.classList.remove('hidden');
    }
    
    // Set the appropriate weather icon based on conditions
    function setWeatherIcon(conditions) {
        weatherIcon.className = ''; // Clear existing classes
        
        switch (conditions) {
            case 'Clear':
                weatherIcon.className = 'fas fa-sun';
                break;
            case 'Clouds':
                weatherIcon.className = 'fas fa-cloud';
                break;
            case 'Rain':
            case 'Drizzle':
                weatherIcon.className = 'fas fa-cloud-rain';
                break;
            case 'Thunderstorm':
                weatherIcon.className = 'fas fa-bolt';
                break;
            case 'Snow':
                weatherIcon.className = 'fas fa-snowflake';
                break;
            case 'Mist':
            case 'Fog':
            case 'Haze':
                weatherIcon.className = 'fas fa-smog';
                break;
            default:
                weatherIcon.className = 'fas fa-cloud-sun';
        }
    }
    
    // Show loading state
    function showLoading() {
        resultSection.classList.add('hidden');
        errorSection.classList.add('hidden');
        loadingSection.classList.remove('hidden');
    }
    
    // Hide loading state
    function hideLoading() {
        loadingSection.classList.add('hidden');
    }
    
    // Show error message
    function showError(message) {
        errorMessage.textContent = message;
        resultSection.classList.add('hidden');
        loadingSection.classList.add('hidden');
        errorSection.classList.remove('hidden');
    }
    
    // Reset the form to try again
    function resetForm() {
        resultSection.classList.add('hidden');
        errorSection.classList.add('hidden');
        moodSelect.value = '';
        cityInput.value = '';
    }
});