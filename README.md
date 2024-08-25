# AI-Driven Content Creation with IBM Watsonx.ai

## Overview

This project showcases an AI-driven content creation tool that utilizes IBM's Granite model via the watsonx.ai platform. The application, developed using Streamlit, allows users to generate personalized marketing content efficiently, enhancing their marketing strategies.

## Features

- **User-Friendly Interface:** Navigate seamlessly through the application to input company details and generate content.
- **Customizable Inputs:** Specify details such as industry type, target audience, and brand voice for tailored content.
- **Real-Time Content Generation:** Generate high-quality, personalized content on demand.
- **Actionable Recommendations:** Receive insights and recommendations to refine marketing strategies.

## Technology Stack

- **Frontend:** Streamlit
- **Backend:** IBM Granite model via watsonx.ai
- **Scripting Language:** Python

## Getting Started

To get started with this project, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Atif-11/creative-catalysts.git
   ```

2. **Set Up Environment**

   Create a `.env` file in the root directory of the project with the following content:

   ```
   IBM_API_KEY=your_ibm_api_key
   IBM_SERVICE_URL=your_ibm_service_url
   IBM_PROJECT_ID=your_ibm_project_id
   IBM_Access_Token=your_ibm_access_token
   ```

   **Note:** Ensure to replace placeholder values with your actual IBM API credentials.

3. **Install Dependencies**

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   Start the Streamlit application:

   ```bash
   python -m streamlit run main.py
   ```

   Open your browser and go to `http://localhost:8501` to interact with the application.

## Usage

1. **Navigate to Company Details Page:**
   - Enter company information including name, industry type, target audience, brand voice, and key products.
   - Save the details to proceed to content generation.

2. **Generate Content:**
   - Choose the type of content (Social Media Post, Email, Ad Copy).
   - Provide relevant details such as product name, description, and features.
   - Click on "Generate Content" to see the output.

3. **View Recommendations:**
   - The application will also generate actionable recommendations to enhance your marketing strategy.

## Project Structure

- `main.py`: The main application script.
- `.env`: Configuration file for environment variables (hidden in the repository).

## Contributing

Feel free to fork the repository and submit pull requests. We welcome contributions to improve the application.

## License

This project is licensed under the MIT License. See the [MIT LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please reach out to:

- Sayyed Muhammad Atif Ali - [atif42068@gmail.com](mailto:atif42068@gmail.com)
