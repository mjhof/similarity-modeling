def show_gt_description(df, column, fps=25):
    print(f"Video: {df.loc[0, 'Video']}")
    print(f"Number of frames: {df['Frame_number'].count()}")
    print(f"Number of frames with Swedish Chef in audio: {df.loc[df[column] == 1, 'Frame_number'].count()}")
    print(f"Length: {len(df['Frame_number']) / fps} seconds")

    # plotting with frames and seconds as x-axis
    fig = plt.figure(figsize=(8, 3))
    ax1 = fig.add_subplot(111)
    ax1.set_title(f"Frames where {column} occurs in audio for video {df.loc[0, 'Video']}")
    ax1.set_xlabel('Frames')
    frame_indicator = np.zeros(len(df['Frame_number']))
    frame_indicator[df[df[column] == 1].index] = 1
    ax1.plot(df[column].index, frame_indicator)

    def frames_to_sec(x):
        return x / fps

    def sec_to_frames(x):
        return x * fps

    ax2 = ax1.secondary_xaxis('top', functions=(frames_to_sec, sec_to_frames))
    ax2.set_xlabel('Seconds')
    plt.show()
