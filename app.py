export default function EcoFriendApp() {
  const features = [
    {
      title: "🌱 Plant Recommendation",
      telugu: "మొక్కల సిఫార్సు",
      desc: "Get the best plant based on climate and sunlight.",
    },
    {
      title: "🪴 Soil Guidance",
      telugu: "మట్టి సూచనలు",
      desc: "Know the best soil type and water quantity.",
    },
    {
      title: "🍂 Disease Detection",
      telugu: "ఆకు వ్యాధి గుర్తింపు",
      desc: "Upload leaf images for disease prediction.",
    },
    {
      title: "🤖 AI Chatbot",
      telugu: "ఏఐ చాట్‌బాట్",
      desc: "Ask doubts about plants in English & Telugu.",
    },
    {
      title: "📈 Growth Prediction",
      telugu: "వృద్ధి అంచనా",
      desc: "Predict plant growth using AI.",
    },
    {
      title: "🎤 Voice Assistant",
      telugu: "వాయిస్ అసిస్టెంట్",
      desc: "Regional language voice support.",
    },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-b from-green-50 to-green-200 text-gray-800">
      {/* HERO SECTION */}
      <section className="flex flex-col items-center justify-center text-center px-6 py-16">
        <div className="bg-white/70 backdrop-blur-lg shadow-2xl rounded-3xl p-10 max-w-5xl border border-green-200">
          <h1 className="text-5xl font-extrabold text-green-800 mb-4">
            🌿 EcoFriend
          </h1>

          <h2 className="text-2xl font-semibold text-green-700 mb-6">
            AI Smart Plantation Assistant
          </h2>

          <p className="text-lg text-gray-700 leading-8">
            An AI-based smart plantation app that helps students choose
            plants, detect diseases, predict growth, and learn plant care.
          </p>

          <p className="mt-4 text-xl font-medium text-green-800">
            విద్యార్థుల కోసం రూపొందించిన స్మార్ట్ ప్లాంటేషన్ యాప్ 🌱
          </p>

          <div className="mt-8 flex gap-4 justify-center flex-wrap">
            <button className="bg-green-700 hover:bg-green-800 transition-all duration-300 text-white px-8 py-3 rounded-2xl text-lg shadow-lg">
              Login
            </button>

            <button className="bg-white border-2 border-green-700 hover:bg-green-100 transition-all duration-300 text-green-800 px-8 py-3 rounded-2xl text-lg shadow-lg">
              Create Account
            </button>
          </div>
        </div>
      </section>

      {/* AUTH SECTION */}
      <section className="px-6 pb-16">
        <div className="max-w-4xl mx-auto bg-white shadow-2xl rounded-3xl p-10 border border-green-100">
          <h2 className="text-3xl font-bold text-center text-green-800 mb-8">
            🔐 Authentication Page
          </h2>

          <div className="grid md:grid-cols-2 gap-8">
            {/* LOGIN */}
            <div className="bg-green-50 p-6 rounded-2xl shadow-lg">
              <h3 className="text-2xl font-bold text-green-700 mb-4">
                Login
              </h3>

              <input
                type="text"
                placeholder="Username"
                className="w-full p-3 rounded-xl border border-green-300 mb-4"
              />

              <input
                type="password"
                placeholder="Password"
                className="w-full p-3 rounded-xl border border-green-300 mb-4"
              />

              <button className="w-full bg-green-700 hover:bg-green-800 text-white py-3 rounded-xl transition-all duration-300">
                Next ➜
              </button>
            </div>

            {/* CREATE ACCOUNT */}
            <div className="bg-green-50 p-6 rounded-2xl shadow-lg">
              <h3 className="text-2xl font-bold text-green-700 mb-4">
                Create Account
              </h3>

              <input
                type="text"
                placeholder="Full Name"
                className="w-full p-3 rounded-xl border border-green-300 mb-4"
              />

              <input
                type="email"
                placeholder="Email"
                className="w-full p-3 rounded-xl border border-green-300 mb-4"
              />

              <input
                type="password"
                placeholder="Password"
                className="w-full p-3 rounded-xl border border-green-300 mb-4"
              />

              <button className="w-full bg-green-700 hover:bg-green-800 text-white py-3 rounded-xl transition-all duration-300">
                Register 🌱
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* FEATURES SECTION */}
      <section className="px-6 pb-20">
        <div className="text-center mb-12">
          <h2 className="text-4xl font-bold text-green-900">
            ✨ Features
          </h2>

          <p className="mt-4 text-lg text-green-800">
            Smart AI-powered tools for plant care.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-8 max-w-7xl mx-auto">
          {features.map((feature, index) => (
            <div
              key={index}
              className="bg-white/80 backdrop-blur-lg rounded-3xl p-8 shadow-2xl border border-green-100 hover:scale-105 transition-all duration-300"
            >
              <h3 className="text-2xl font-bold text-green-800 mb-2">
                {feature.title}
              </h3>

              <h4 className="text-lg text-green-600 mb-4">
                {feature.telugu}
              </h4>

              <p className="text-gray-700 leading-7">
                {feature.desc}
              </p>

              <button className="mt-6 bg-green-700 hover:bg-green-800 text-white px-6 py-2 rounded-xl shadow-lg transition-all duration-300">
                Open Feature
              </button>
            </div>
          ))}
        </div>
      </section>

      {/* FOOTER */}
      <footer className="bg-green-900 text-white text-center py-8">
        <h3 className="text-2xl font-bold mb-2">🌿 EcoFriend</h3>

        <p>
          Smart Plantation Assistant for Students | విద్యార్థుల కోసం
          స్మార్ట్ ప్లాంటేషన్ యాప్
        </p>
      </footer>
    </div>
  );
}
