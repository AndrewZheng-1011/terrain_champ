#ifndef QUADRUPED_DESCRIPTION_H
#define QUADRUPED_DESCRIPTION_H

#include <quadruped_base/quadruped_base.h>

namespace champ
{
    namespace URDF
    {
        void loadFromHeader(champ::QuadrupedBase &base)
        {
      base.lf.hip.setOrigin(0.0295965121886, 0.047, 0.0, 0.0, 0.0, 0.0);
base.lf.upper_leg.setOrigin(0.0152498678114, 0.02535, -0.0, 0.0, 0.0, 0.0);
base.lf.lower_leg.setOrigin(0.0, 0.0, -0.0799999971868, 0.0, 0.0, 0.0);
     base.lf.foot.setOrigin(0.0, 0.008325, -0.11, 0.0, 0.0, 0.0);

      base.rf.hip.setOrigin(0.0294749675165, -0.047, 0.0, 0.0, 0.0, 0.0);
base.rf.upper_leg.setOrigin(0.0152520324835, -0.02535, -0.0, 0.0, 0.0, 0.0);
base.rf.lower_leg.setOrigin(0.0, 0.0, -0.0799999971868, 0.0, 0.0, 0.0);
     base.rf.foot.setOrigin(0.0, -0.008325, -0.11, 0.0, 0.0, 0.0);

      base.lh.hip.setOrigin(-0.12912862, 0.047, 0.0, 0.0, 0.0, 0.0);
base.lh.upper_leg.setOrigin(-0.026025, 0.02535, -0.0, 0.0, 0.00113054427428, 0.0);
base.lh.lower_leg.setOrigin(0.0, 0.0, -0.0799999971868, 0.0, -0.00113054427428, 0.0);
     base.lh.foot.setOrigin(0.0, 0.008325, -0.11, 0.0, 0.0, 0.0);

      base.rh.hip.setOrigin(-0.129248, -0.047, 0.0, 0.0, 0.0, 0.0);
base.rh.upper_leg.setOrigin(-0.026025, -0.02535, -0.0, 0.0, 0.0, 0.0);
base.rh.lower_leg.setOrigin(0.0, 0.0, -0.0799999971868, 0.0, 0.0, 0.0);
     base.rh.foot.setOrigin(0.0, -0.008325, -0.11, 0.0, 0.0, 0.0);
        }
    }
}
#endif