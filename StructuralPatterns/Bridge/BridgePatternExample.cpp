#include <iostream>
#include <string>

// Implementation interface
class Device {
public:
    virtual std::string play_audio() = 0; // Abstract method to play audio
};

// Concrete Implementations
class Speaker : public Device {
public:
    std::string play_audio() override {
        return "the Speaker";
    }
};

class Headphones : public Device {
public:
    std::string play_audio() override {
        return "the Headphones";
    }
};

// Abstraction
class MusicPlayer {
public:
    MusicPlayer(Device* device) : device(device) {}

    std::string play() {
        return "Playing music on " + device->play_audio();
    }

private:
    Device* device; // Reference to implementation
};

// Extended Abstraction
class AdvancedMusicPlayer : public MusicPlayer {
public:
    AdvancedMusicPlayer(Device* device) : MusicPlayer(device) {}

    std::string play() {
        return "Playing music with equalizer on " + MusicPlayer::play();
    }
};

// Client code
void client_code(MusicPlayer* musicPlayer) {
    std::cout << musicPlayer->play() << std::endl;
}

int main() {
    // Using basic music player with speaker
    Device* device1 = new Speaker();
    MusicPlayer* basicPlayer = new MusicPlayer(device1);
    client_code(basicPlayer);

    // Using advanced music player with headphones
    Device* device2 = new Headphones();
    MusicPlayer* advancedPlayer = new AdvancedMusicPlayer(device2);
    client_code(advancedPlayer);

    // Clean up
    delete device1;
    delete basicPlayer;
    delete device2;
    delete advancedPlayer;

    return 0;
}
