#!/bin/bash

# Parse arguments
DEVICE_TYPE=""
FORCE_BUILD=false

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --build|-b)
            FORCE_BUILD=true
            shift
            ;;
        flex|stax|nanox|nanosplus)
            DEVICE_TYPE="$1"
            shift
            ;;
        *)
            echo "Error: Unknown argument '$1'"
            echo "Usage: $0 [flex|stax|nanox|nanosplus] [--build|-b]"
            echo "Default device: flex"
            echo "Options:"
            echo "  --build, -b    Force rebuild even if app.elf exists"
            exit 1
            ;;
    esac
done

# Set default device type if not provided
DEVICE_TYPE=${DEVICE_TYPE:-flex}

# Validate device type
case "$DEVICE_TYPE" in
    flex|stax|nanox|nanosplus)
        echo "Target device: $DEVICE_TYPE"
        ;;
    *)
        echo "Error: Invalid device type '$DEVICE_TYPE'"
        echo "Usage: $0 [flex|stax|nanox|nanosp] [--build|-b]"
        echo "Default device: flex"
        exit 1
        ;;
esac

# Check if build is needed
BUILD_PATH="build/$DEVICE_TYPE/bin/app.elf"
if [[ -f "$BUILD_PATH" && "$FORCE_BUILD" == false ]]; then
    echo "App already built for $DEVICE_TYPE (found $BUILD_PATH)"
    echo "Skipping build. Use --build or -b to rebuild."
else
    if [[ "$FORCE_BUILD" == true ]]; then
        echo "Force rebuilding for device: $DEVICE_TYPE"
    else
        echo "Building for device: $DEVICE_TYPE (app.elf not found)"
    fi
    
    # Build the app for the specified device
    docker run --rm -v "$(pwd -P):/app" ghcr.io/ledgerhq/ledger-app-builder/ledger-app-dev-tools:latest bash -c "cd ./rust-app/ && cargo ledger build $DEVICE_TYPE -- -Zunstable-options --artifact-dir build/$DEVICE_TYPE/bin && mv build/$DEVICE_TYPE/bin/iota build/$DEVICE_TYPE/bin/app.elf && mv build/$DEVICE_TYPE/bin/iota.apdu build/$DEVICE_TYPE/bin/app.apdu"
    
    # Verify build was successful
    if [[ ! -f "$BUILD_PATH" ]]; then
        echo "Error: Build failed - $BUILD_PATH not found"
        exit 1
    fi
    echo "Build completed successfully"
fi

# Run speculos with the built app
echo "Starting Speculos for $DEVICE_TYPE..."
# Map nanosplus to nanosp for speculos command
SPECULOS_MODEL="$DEVICE_TYPE"
if [[ "$DEVICE_TYPE" == "nanosplus" ]]; then
    SPECULOS_MODEL="nanosp"
fi
docker run --rm -it --privileged -v "$(pwd -P):/app" --publish 5001:5001 --publish 9999:9999 -e DISPLAY='host.docker.internal:0' -v '/tmp/.X11-unix:/tmp/.X11-unix' ghcr.io/ledgerhq/ledger-app-builder/ledger-app-dev-tools:latest bash -c "speculos --model $SPECULOS_MODEL /app/build/$DEVICE_TYPE/bin/app.elf --apdu-port 9999 --api-port 5001"